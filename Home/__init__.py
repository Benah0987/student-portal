"""
Outer package marker for the project.

This file makes the outer `Home/` directory a Python package so the
existing import path `Home.Home.settings` (used by `manage.py`) works
when running Django from the repository root.
"""

__all__ = []
