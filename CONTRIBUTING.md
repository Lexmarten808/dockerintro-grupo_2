# Contributing (trunk-based development)

We work in the **team fork**, never in the original repository.

## Rules
1. `main` is the trunk. It must always be in a working state.
2. Create a **short-lived branch** from `main`: `student/<your-name>`.
3. Work **only** inside `/students/<your-name>/`.
4. Keep PRs **small** and merge them within a day or two.
5. Open the PR against **this team fork main** (not `fredyunivalle/dockerintro`).
6. At least **one teammate reviews** every PR. Do not merge unreviewed Copilot code.
7. Delete your branch after merging (automatic if enabled in repo settings).

## Workflow
1. Create your neighborhood network on your machine (once):
```
   docker network create <your-neighborhood>
```
   If Docker says it already exists, that's fine. The shared volume
   `biblioteca-del-pueblo` is created automatically the first time you run your container.
2. Create your Issue using the **Student service** template.
3. Assign the Issue to **Copilot** (or use Copilot in your editor if the agent is unavailable).
4. `git checkout main && git pull && git checkout -b student/<your-name>`
5. Review and test the code locally.
6. Open the PR, link the Issue (`Closes #N`), request a review.
7. After merge: build, tag and push your image, run the container, collect evidence.

## Naming conventions
- Folder: `/students/<your-name>/`
- Container: `svc-<your-name>`
- Image: `<registry-user>/cali-service:v1`

## Keeping the fork in sync (leader only)
```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

## Deliverables checklist (collect evidence as you go)
- [ ] Folder with Dockerfile, code and dependencies
- [ ] Your GitHub Issue
- [ ] Evidence of Copilot participation
- [ ] Pull Request linked to the Issue
- [ ] Published Docker image
- [ ] Running container in your neighborhood
- [ ] Build and push evidence
- [ ] Network connectivity test evidence
- [ ] Evidence of writes to `biblioteca-del-pueblo`
- [ ] Short explanation of your design choice