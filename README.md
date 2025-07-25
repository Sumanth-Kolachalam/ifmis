# IFMIS

### Prerequisites

The following apps has to be installed in your development environment

- frappe
- erpnext
- hrms

run this to install the apps

```bash
bench get-app https://github.com/frappe/erpnext

bench --site yoursite install-app erpnext
```

```bash
bench get-app https://github.com/frappe/hrms

bench --site yoursite install-app hrms
```

### Installation

You can install IFMIS app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch dev
bench install-app ifmis
```

### Migrate

To get all the doctypes and the data

``` bash
bench --site sitename migrate
```
