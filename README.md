# workflow_demo

## How to run

Checkout the repository.

-   ***If on Windows:*** run run.bat from the root directory
-   ***If on Linux:*** run run.sh from the root directory

Both will install venv and create a virtual environment, install all required
packages, run the test suite and last but not least start the development server.

The Api can be browsed via /swagger, the spec document is available under /swagger.json .

## Dreaded 403

Due to it being a very small, basic demo, a very basic authentication is in place,
requiring an api key appended to the rest-action.

You can find a predefined user under ***http://{your host}/users***, just copy the api_key and append
it via ***http://{your host}/workflows/?api_key={the copied key}***.

## How to use

Most stuff is centered around workflows, being nested resources of the before mentioned workflows.

-   *http://{your host}/workflows*: a get delivers a list of available workflows, a post creates a new workflow, steps can be nested as per spec
-   *http://{your host}/workflows/{workflow_id}*: a get returns a specific workflow, a patch updates it, a delete deletes it
-   *http://{your host}/workflows/{workflow_id}/comments*: get returns a list of comments appending to the current workflow, a post creates a new comment
-   *http://{your host}/workflows/{workflow_id}/comments/{comment_id}*: a get returns a specific comment, a patch updates it, a delete deletes it
-   *http://{your host}/users*: a get delivers a list of available users, a post creates a new user, the api_key will automatically generated