# DevOps Practical Midterm (PRACTICE PAPER)

**Time:** 60 minutes | **Total marks:** 50
**Rules:** No ChatGPT/AI. Allowed: man pages, `--help`, official docs, your own notes.
Marks are for WORKING output only. A task that does not run earns no credit.

Replace `<roll>` with your roll number in lowercase (e.g. `21sw045`),
`<NN>` with the last two digits of it (e.g. `45`),
and `<user>` with your Docker Hub username.

---

## Task 1: Git and GitHub (10 marks)

1. Create a NEW GitHub repo named `devops-midterm-<roll>`.
2. Put all files from this folder into it (`app.py`, `requirements.txt`, `access.log`, `.gitignore`).
3. Create a branch `feature-<roll>`.
4. Add a file `STUDENT.txt` containing your name and roll number.
5. Commit with the exact message: `Add student info for <roll>`
6. Push the branch and open a Pull Request into `main`.

**Proof:** repo link + PR link.

---

## Task 2: Dockerfile and Docker Hub (10 marks)

Write a `Dockerfile` for `app.py`:

- Base image: `python:3.11-slim`
- Working directory `/app`
- Install dependencies from `requirements.txt` (copy this file BEFORE the rest of the code)
- Copy the app code
- Document port 5000
- Start the app with `python app.py`

Then:

- Build and tag it as `<user>/hitcounter-<roll>:v1`
- Push it to Docker Hub

**Proof:** `docker images` output + Docker Hub page screenshot.

---

## Task 3: Run a container (5 marks)

Run your image in the background with:

- port mapping: host `50<NN>` to container `5000`
- environment variable `APP_NAME=<roll>`
- container name `web-<roll>`

Then:

- `curl localhost:50<NN>/health` must show your roll number
- Show the container logs with `docker logs`

(`/` will return a "redis not reachable" error here. That is expected for now.)

**Proof:** curl output + logs output.

---

## Task 4: Docker Compose (15 marks)

Write `docker-compose.yml` with:

- Service `web`: built from your Dockerfile, port `50<NN>:5000`, environment `APP_NAME=<roll>` and `REDIS_HOST=redis`
- Service `redis`: image `redis:alpine`, data stored in a NAMED volume mounted at `/data`
- A custom network used by both services
- `depends_on` for web

Then:

1. `docker compose up -d`
2. `curl localhost:50<NN>/` three times. Hits must go 1, 2, 3.
3. `docker compose down`
4. `docker compose up -d` again
5. `curl` again. Counter must continue from the old value (4), NOT restart from 1.

**Proof:** terminal output of all steps.

---

## Task 5: Linux commands (10 marks)

Using `access.log`:

1. Count lines containing `404`.
2. Show the top 3 IP addresses by number of requests (use `awk`, `sort`, `uniq`).
3. Using `awk`, calculate the total of the last column (bytes).
4. Save the answer of step 2 into `report.txt`, then set its permissions so owner can read/write, group can read, others have nothing.
5. Create a symbolic link `latest.log` to `access.log`, and a hard link `backup.log` to `access.log`.
6. Run `ls -l` and explain in your own words why `backup.log` and `latest.log` look different.

**Proof:** commands + outputs.

---

## Viva questions (be ready!)

- Why did you copy `requirements.txt` before the app code in the Dockerfile?
- What is the difference between `-p` and `EXPOSE`?
- What happens to data when you run `docker compose down -v`?
- Symbolic link vs hard link: what happens if the original file is deleted?
- What does `git push` do if the branch does not exist on the remote yet?
