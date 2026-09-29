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
2. Open `docs/relationships/open-comments.md`. The **Status summary** at the top lists the comments you can work on.
   Take the next **Ready** one whose box is still `- [ ] applied`. Do **Draft** ones only after the Ready ones are done.
3. In the Claude panel, type:
   > Fix comment AAAB4xFXrvE

   using the real ID. Claude follows the procedure in `CLAUDE.md`.
4. **Claude will show you a proposal and wait.** Read it:
   - Does the "current text" match what the comment is about?
   - Does the replacement do what Sadaf asked, and nothing more?
   - If it's a relationship verb, check it exists in Innoslate's relationship dropdown.

   If all is well, reply **go**. If not, tell Claude what to change, or reply **stop**.
5. After Claude applies it, open **Source Control** (Ctrl+Shift+G) and click each changed file to see old and new side by side.
   - The change should be at one spot only.
   - The comment's box in `open-comments.md` should now be `[x]`.
6. Happy with it? Type the comment ID as the message and click **Commit**. For a **Draft** comment, start the message
   with `DRAFT:`, e.g. `DRAFT: AAAB6wHzTzc`, so Munzir knows to review it. If VS Code asks whether to stage all changes, say **Yes**.
   Not happy? Right-click each file and choose **Discard Changes**. Nothing is lost.
7. Click **Sync** to push.

One comment, one commit. Small commits are what make mistakes easy to undo.

Skip every comment marked **Find in Google Doc** or **Munzir decides**. Claude will refuse them anyway.

## When to stop and ask Munzir

- Claude says it can't find the text, or finds it more than once.
- A fix would need changes in more than one place.
- Source Control shows a file you didn't expect to change.
- Anything says `main`.
