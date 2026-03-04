# Observability

Building observable systems enables development teams at ESF Engineering to measure how well the application is behaving.

## Goals

- Provide a holistic view of the **application health**
- Help measure **business performance** for the customer
- Measure **operational performance** of the system
- Identify and **diagnose failures** to get to the problem fast

## Pillars of Observability

- **Logs** — Discrete events with the goal of helping engineers identify problem areas during failures
- **Metrics** — Point-in-time measurements of a particular source; compact and efficient for alerting
- **Traces** — Follow a program's flow and data progression across distributed systems
- **Dashboards** — Aggregation and visualization of the above signals

---

## Signals: Logs vs Metrics vs Traces

### Metrics

Metrics represent a point-in-time measurement of a particular source. Their compact size allows efficient collection at scale and they lend themselves well to pre-aggregation and automated alerting. Use metrics to track the occurrence of an event, counts, timing, or resource utilization (CPU, memory, etc.).

### Logs

Log data informs observers about discrete events within a component. Rich but potentially large — using log data to understand health of an extensive system tends to be avoided in favor of metrics for health data. Once metrics highlight a potential problem source, filtered log data helps understand what occurred. Use logs to track detailed information about events, particularly errors, warnings, or exceptional situations.

### Traces

Traces follow a program's flow and data progression across an entire app stack. Each trace is composed of spans — the smallest unit representing a piece of workflow (e.g., an HTTP request, a database call, a queue message). Use traces to understand distributed request flows, identify bottlenecks, and optimize performance. Every trace needs a unique identifier (Correlation ID).

**When to use each:**

| Signal | Use when... |
|--------|-------------|
| Metrics | Tracking occurrence of events, counts, timings, resource utilization |
| Logs | Recording detailed info about events, especially errors and exceptional situations |
| Traces | Understanding how a request is processed across multiple services |

---

## Recommended Practices

1. **Correlation ID** — Include a unique identifier at the start of each interaction to tie together aggregated data from various system components. Pass this ID through all services in a distributed system to enable end-to-end tracing.
1. **Monitor service health** — Ensure health of services is monitored with insights into system performance and behavior.
1. **Monitor dependent services** — Errors and exceptions in dependent services (Redis cache, Service Bus, etc.) should be logged and alerted; metrics should be captured.
1. **Log faults, crashes, and failures as discrete events** — This helps engineers identify problem areas during failures.
1. **Make logging configuration controllable without code changes** — Ideally without application restarts.
1. **Collect latency and duration metrics** — Ensure these metrics can be aggregated.
1. **Start small and add where there is customer impact** — Avoid metric fatigue by collecting actionable data only.
1. **Include relevant and rich context** in every data point collected.
1. **Never log PII or customer sensitive information** — Follow local privacy regulations (e.g., GDPR).
1. **Add appropriate health checks** — Determine if a service is healthy and ready to serve traffic (e.g., Kubernetes liveness, readiness, startup probes).

---

## Logging Best Practices

### Log Levels

- Pay attention to logging levels — logging too much increases costs and decreases throughput.
- Fine-tune log levels in production (`>= warning` by default). During new releases, increase verbosity to facilitate bug identification.
- If available, use per-category log levels for granular configuration.
- Check log levels before logging to avoid unnecessary string manipulation costs.

### PII and Privacy

- Ensure personal identifiable information policies and restrictions are followed — never log PII.
- Scrub URLs of PII before logging (e.g., user IDs in query strings).

### What to Log

**At application startup:**

- Unrecoverable errors
- Warnings if the application is still runnable but not as expected
- Service state at startup (build #, configs loaded, etc.)

**Per incoming request:**

- URL (scrubbed of PII), user/tenant/request dimensions, response code, request-to-response latency, payload size
- Unexpected exceptions at the top controller/interceptor (with stack trace); return a 500

**Per outgoing request:**

- URL (scrubbed of PII), response code, latency, payload size; perceived availability and latency of dependencies

**Additional guidance:**

- Log a raised exception only once — at the top-level handler, not at every catch block
- Ensure service versions are included in logs to identify problematic releases
- Ensure errors and exceptions in dependent services (Redis, Service Bus, etc.) are captured and logged

### Recommended Tools

- [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/overview) — Umbrella of services including system metrics, log analytics, and more
- [Grafana Loki](https://grafana.com/oss/loki/) — Open source log aggregation platform, highly efficient at scale
- [The Elastic Stack](https://www.elastic.co/what-is/elk-stack) — Open source log analytics stack (Logstash, Beats, Elasticsearch, Kibana)
- [Grafana](https://grafana.com) — Open source dashboard and visualization; supports Logs, Metrics, and Distributed Tracing
- [OpenTelemetry](https://opentelemetry.io/) — Vendor-neutral standard for instrumentation, collection, and export of telemetry data
