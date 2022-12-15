# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.5] - 2022-12-15
### Added
- `Bool` field

## [0.3.4] - 2022-05-01
### Fixed
- `async_timeout` cancels the timeout task if an exception is being raised in the main task

## [0.3.3] - 2022-05-01
### Added
- `AsyncWorker`
- `async_timeout`

## [0.3.2] - 2022-03-27
### Added
- Typing
- `env_config.BaseConfig` class supports `typing.Optional` in class variables

## [0.3.1] - 2022-02-20
### Added
- `datek_app_utils.env_config.BaseConfig` supports default value in it's fields

## [0.3.0] - 2021-11-14
### Changed
- Breaking change: `validate_config()` now raises error instead of returning `bool`
- `validate_config()` now doesn't log anything

### Added
- `black` formatting
- `changelog.md`