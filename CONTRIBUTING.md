# Contributing

Demonstrating Engineering Fundamentals is core to what we do at ESF and is one of the primary values we bring to our customers, helping them to level up while collaborating on their business scenarios.

The purpose of this repo is to provide guidance to ESF software engineers with regards to engineering fundamentals. It describes recommended practices based on continuous project learnings in different areas. It can be used as a tool at the beginning of an engagement that can be shared with customers to help set the project up for success. This repo is *not* intended as a code repo, instead it provides guidance and links to appropriate sample code repos that represent good examples.

This project welcomes contributions and suggestions.

## What to contribute

- Patterns and practices that have worked well in engagements, related to our engineering fundamentals
- Content that can be publicly visible (avoid confidential information)
- Content that is generally applicable (avoid references to internal processes, or very specific information)

## General guidance

- Quality is more important than quantity
- Write in a way that you would want someone else to explain something to you. Use [`plain english`](http://www.plainenglish.co.uk/how-to-write-in-plain-english.html)
- Be friendly, technical, professional and concise
- Communicate as engineers, not marketing; we want to share what we learned, not "sell" our ideas
- Don't recreate introductory content, link to it
- Add context around patterns, recipes etc. so that the reader understands when and where a pattern may be applicable and where it may not
- Think about how readers can discover your content, is it easy to find?

> NOTE: Please discuss with one of the [maintainers](#maintainers) before adding a new top level section. Try to find a suitable home in an existing section if possible.

We welcome maintenance of the repository and contributions that:

- Makes the content more readable
- Makes the content more discoverable
- Fixes content that has gone out-of-date

or anything that improves the quality of the playbook

## How to contribute

### Submitting a PR

- Add your changes to a new branch `<github alias>/<title>` or by forking the repository
- Open a PR with a clear description of the changes
- Tag the PR with the appropriate area, and link any issues that the PR closes
- Add reviewers (you will need 2 reviewers to merge) to the PR, for example the [maintainers](#maintainers) or anyone from the [EF champs team](https://github.com/esf/engineering-playbook/blob/main/.github/CODEOWNERS)

### Link checks

Before a pull request can be merged, any links in the documents will be checked to make sure that they are still live.

On occasion, you will find that the link checker will fail on links that you can reach fine with a browser. It may also fail on links that are not in the documents that you submitted changes to.

When this occurs, do the following

1. Verify that the link is OK, if it redirects, change the path to be the final link.
1. If the link is not ok, fix the link (even if it is not in your document) if you find a good equivalent link. If you can't find a good equivalent link, contact one of the [maintainers](#maintainers) for a solution.
1. Re-run the job, or ask to have the job re-run (if you are a first time contributor). Sometimes the link checker fails due to temporary connectivity issues.
1. If the link checker still fails, and you have confirmed that the link is ok, exclude the link from checking in the [lychee.toml](./lychee.toml) file.

## Running Locally (*Remotely*)

To run the site locally, you must have [VSCode](https://code.visualstudio.com/), [Docker](https://www.docker.com/), and the [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) installed on your machine.

After cloning this repo, open it in VSCode. Open the VSCode command prompt using `CTRL/CMD + SHIFT + P` and run the `Remote-Container: Rebuild and Reopen in Container` command (make sure Docker is also running on your machine).

After sometime, VSCode should reopen this repository in the remote dev container and install the required dependencies.

Finally, launch the site locally using the `mkdocs serve` command from the root of the repo.

## Maintainers

For any questions or concerns, please contact [Jim Ramia](mailto:jim.ramia@esolutionsfirst.com), [Vikram Ekollu](mailto:vikram.ekollu@esolutionsfirst.com) or [Amine Khammal](mailto:amine@esolutionsfirst.com).

