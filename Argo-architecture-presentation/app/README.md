# GITOPS:
GitOps upholds the principle that Git is the one source of truth.

The Kubernetes API server accepts a declaration as an input (.yaml/.yml), and then 
continually tries to drive (or converge) the cluster to the desired state 
described in the declaration.

Git commits cause verifiable updates to the Kubernetes cluster.

Declarative Kubernetes Files saved in git, in yaml formats

DAN:
(Gitops repo is esperated from the code argo looks at the HELM, *add a helm/ yml/ jsonnet image for page 5*)
DAN:


# ArgoCD: THE solution to kubernetes ContinuousDelivery
https://argo-cd.readthedocs.io/en/stable/

DAN:
(argo permorms the gitops in kubernetes, which is a block box for the developers)
(git push, apply webhook, trigger an ansible script)
DAN:


Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes.

supports: kustomize applications, helm charts, jsonnet files, Plain directory of YAML/json manifests

Argo CD is implemented as a kubernetes controller which continuously monitors running 
applications and compares the current, live state against the desired target state.

A deployed application whose live state deviates from the target state is considered OutOfSync.

Argo CD reports & visualizes the differences, while providing facilities to automatically or manually
sync the live state back to the desired target state. Any modifications made to the desired target
state in the Git repo can be automatically applied and reflected in the specified target environments.





# DEMO:
## Create cluster GKE (Not auto pilot)

###
kubectl get node

kubectl create namespace argocd

kubectl get ns

kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
(40 seconds on first run)

kubectl port-forward svc/argocd-server -n argocd 8080:443
(port-forward) - ingress 


kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d



###

- upload argocd - helm add 

- add application as yaml (save time and show values in summary) 

- 

- show created objects

- example: commit a change, show sync process (try adding webhook to apply a sync, so theres no 
need for polling)

- 

- example: pod (no deployment) to show argo keeps watching git objects kubernetes 'forgot about'

- Rollback


DAN:

**
app write a sentence in the config map:
"hello world!"
"the source is now git"
"the source is now override" - override through argo
+
for loop with sleep to write to logs
"" 
mount logs in to volume
we changed, we dont even need jenkins for it.
חוסך גובים של גנקינז
DAN:




# for app:

# export MESSAGE='lala land is great!' , in terminal

# to run docker with container, bash:
# version=3 && docker  build -t argo-demo-app:$version . && docker tag argo-demo-app:$version eu.gcr.io/python-argo/argo-demo-app:$version && docker push eu.gcr.io/python-argo/argo-demo-app:$version
# docker run -it --name=argo-demo -e MESSAGE="is it saved?" -v argo-demo-log:/var/log argo-demo-app:2
