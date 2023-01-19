# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).


## [0.0.2] - 2023-01-18

### Added

- `Countdown` added as alias for `Formatter` in package init.

### Changed

- Updated package name to `countdown` now that the name is available on the Python Package Index.
- `Formatter` class in package init no longer imported as `Countdown`.
- `Formatter.default_formatter` no longer includes the `z` flag.

### Fixed

- Incorrect format string in `Formatter.default_formatter`.
