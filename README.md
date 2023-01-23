# immutable-file-Action
This GitHub Action ensures that selected project files remains consistent and unmodified by automatically detecting and preventing any changes to specified files and directories.

For example, if your `Dockerfile` folder to be immutable

```
files:
    Dockerfile
```

If you want the `.github` folder to be immutable

```
files:
    .github
```

And if you want all the files that end with `yml` in the `.github` folder

```
files:
    .github/.*.yml
```

By default, this action uses regex to validate and add the `^` operator to the start.

## Inputs

### `files`

An array of regex to validate from. 

## Example Usage

```
- name: Immutable Files
  uses: asafHalely/immutable-file-action@v1
```

## Example Usage with a specific Project Key

```
- name: Immutable Files
  uses: asafHalely/immutable-file-action@v1
  with:
    files:
        Dockerfile
        .github/.*.yml
```
