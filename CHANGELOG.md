# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of gotty-py client
- WebSocket client for gotty terminal interfaces
- Basic authentication support
- Command execution with response handling
- Terminal output buffering and history
- Real-time callback system for output and commands
- Threading support for background operations
- Comprehensive test suite with unit and integration tests
- Example scripts for basic and advanced usage
- GitHub Actions CI/CD pipeline
- Modern Python packaging with pyproject.toml
- Development tools: black, mypy, flake8, isort
- Makefile for common development tasks

### Features
- Generic gotty protocol support
- WebSocket communication with gotty servers
- HTTP basic authentication
- Command execution with timeout support
- Terminal output history management
- Thread-safe operations
- Real-time output and command callbacks
- Connection state management
- Error handling and logging

### Technical Details
- Python 3.8+ support
- Async/await WebSocket handling
- Threading for background message processing
- Base64 encoding/decoding for terminal output
- Comprehensive error handling and logging
- Type hints throughout the codebase
- Extensive unit test coverage
- Integration tests for real server interaction
