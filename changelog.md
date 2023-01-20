# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Changed

- Formatter code is now in a separate file.
- Slight changes to constant names.
- The format string pre-format function now includes the `z` flag in all flags.
- Name of `Formatter` is now just `Countdown`.
- Some values in `Countdown` (such as the updated and original formats) are stored privately and
  can be accessed through properties.

### Added

- Added `utils.py` for the `StaticProperty` class.
- Added `models.py` for the `TimeValue` class.

## [0.0.2] - 2023-01-18

### Added

- `Countdown` added as alias for `Formatter` in package init.

### Changed

- Updated package name to `countdown` now that the name is available on the Python Package Index.
- `Formatter` class in package init no longer imported as `Countdown`.
- `Formatter.default_formatter` no longer includes the `z` flag.

### Fixed

- Incorrect format string in `Formatter.default_formatter`.
