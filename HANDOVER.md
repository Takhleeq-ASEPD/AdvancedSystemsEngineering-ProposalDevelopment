# Handover: fixing Sadaf's open comments

For this job, this page replaces Parts 8 and 9 of `SETUP.md`. Everything else in `SETUP.md` still applies.

## The one rule

**Always work on the `restore` branch.** Never switch to `main`, never merge. Munzir merges `restore`
into `main` when the fixes are done. That is what publishes the site.

## First time only

In the VS Code terminal, inside the project folder:

```powershell
git status
git fetch
git checkout restore
git log --oneline -3
```

- `git status` should say there is nothing to commit. If it lists changes, run `git checkout -- .`
- The bottom-left corner of VS Code should now say **restore**.

## Preview address

Start the preview with `mkdocs serve` as in `SETUP.md`, but in Simple Browser use this address.
The plain `http://127.0.0.1:8000` gives a 404.

```
http://127.0.0.1:8000/AdvancedSystemsEngineering-ProposalDevelopment/
```

The comment list is at `.../relationships/open-comments/`.

## Each comment

1. Check the bottom-left corner says **restore**. Click **Sync** (the circling arrows next to it) to get the latest.
2. Open `docs/relationships/open-comments.md`. Pick the next comment with `- [ ] applied`.
3. In the Claude panel, type:
   > Fix comment AAAB6feBJ4M
   
   using the real ID. The rules Claude follows are in `CLAUDE.md`, so that is all you need to say.
4. Open **Source Control** (Ctrl+Shift+G). Click each changed file to see old and new side by side.
   - The change should be at the spot the comment names, and nowhere else.
   - The comment's box in `open-comments.md` should now be `[x]`.
   - If it's a relationship verb, check it against Innoslate's relationship dropdown.
5. Happy with it? Type the comment ID as the message, e.g. `AAAB6feBJ4M: performs`, and click **Commit**.
   If VS Code asks whether to stage all changes, say **Yes**.
   Not happy? Right-click each file and choose **Discard Changes**. Nothing is lost.
6. Click **Sync** to push.

One comment, one commit. Small commits are what make mistakes easy to undo.

## When to stop and ask Munzir

- Claude says it can't find the spot, or the anchor doesn't match the comment.
- A fix would need changes in more than one place.
- Source Control shows a file you didn't expect to change.
- Anything says `main`.
