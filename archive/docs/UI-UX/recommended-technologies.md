# Recommended Technologies

## When to Use What

| Scenario | Recommended Stack | Why |
|----------|-------------------|-----|
| New SPA with complex state, Azure/Entra auth | **React + TypeScript + Vite** | Large ecosystem, MSAL support, team familiarity |
| .NET-first team, server-rendered UI, minimal JS | **Blazor (Server or WASM)** | C# end-to-end, strong .NET/Azure integration |
| Mostly server-rendered with light interactivity | **HTMX + minimal JS** | Low complexity, no build toolchain, good for simple forms/dashboards |

When in doubt: use React. It's the default for greenfield projects at ESF and has the most internal support.

## TypeScript

Use TypeScript for all new web projects. Prefer `type` over `interface` — it's more flexible (supports union types) and avoids unintended inheritance.

## React Quick Start

Bootstrap with [Vite](https://vitejs.dev/), not `create-react-app` (deprecated January 2023):

```sh
npm create vite@latest
```

Use modern React (hooks, function components). If a guide shows class components, it's outdated.

## Key Practices

- **Project structure**: co-locate tests with components (`Button/Button.tsx` + `Button.test.tsx`)
- **Auth**: use [`@azure/msal-react`](https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-react) for Entra ID integration
- **API calls**: use Axios with an interceptor to attach MSAL bearer tokens
- **Env vars**: prefix with `VITE_`, access via `import.meta.env.VITE_*`, never commit `.env`
- **Security**: never store tokens in `localStorage`, avoid `dangerouslySetInnerHTML` without sanitization, keep dependencies updated (`npm audit`)
