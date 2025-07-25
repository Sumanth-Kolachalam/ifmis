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
# Navigate to your bench
cd path/to/your/bench

# Get the app from the github repo
bench get-app https://github.com/Sumanth-Kolachalam/ifmis.git

# Install the app into your site
bench --site yoursite install-app ifmis
```

### Migrate

To get all the doctypes and the data

``` bash
bench --site yoursite migrate
```
