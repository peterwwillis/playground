# Dead Simple CI

(Almost) The simplest possible continuous integration server.


## Design goals
1. Use the simplest possible solution, as long as it enables the other design goals.
2. Be composeable. Components can work individually, be replaced, combined with more components.
3. Use network-agnostic protocols for communication.
4. Easy for anyone to understand how it works
5. Avoid single-host computing paradigms and prefer networked components.
6. Be able to run in any kind of system.

### Design requirements

#### 1. Containers not required
Assume you are a local user in a Linux operating system and just execute commands.
This means you have environment variables, tcp/ip sockets, stdin/stdout/stderr.

#### 2. Do not depend on the filesystem
Most components should not depend on a traditional filesystem. Filesystems limit the
system design by creating dependence on specific pieces of infrastructure which are
difficult to scale and introduce availability concerns. Instead, storage should be
via some network service (ex. AWS S3 compatible) which can abstract away and scale
the storage while also providing strong isolation and consistency guarantees.

### Design

#### 1. Scheduling

#### 2. Execution

#### 3. Storage (storesvc)

The storage service (storesvc) takes a key and a request type, and returns a value.
Multiple keys can be passed at once for requests that only take a key as input.
 - Request type: GET
   - Input arguments: `key`
 - Request type: PUT
   - Input arguments: `key`, `content`
 - Request type: DELETE
   - Input arguments: `key`
 - Request type: LIST
   - Input arguments: `key`

##### Storage: Backend: object store
 - A storage network provider exists (e.g. AWS S3 compatible object storage)
 - storesvc authenticates with storage provider and can create and manage objects
 - storesvc is configured to access one or multiple storage providers
 - storesvc is configured to place certain objects in certain storage providers
 - storesvc uses authnz to authenticate incoming storage requests

###### Storage: Backend: object store: operations
`key`s are an object store path prefix.
`content` is the content to store in, or is retrieved from, and object.

#### 4. Authentication/Authorization (AuthN+Z or authnz)

Since everything is networked, all requests must be authorized.
 - Use some equivalent to a Bearer Token to authorize requests.
 - A service will be dedicated to authenticating a request and returning an authorization token.
 - Each other service will accept an authorization token and verify with the authnz service that the token is valid.
 - The authnz service will return a blob that says what the token is allowed to do (scopes).
 - The service will match a request type against the blob and return an error if the request type is not allowed.

