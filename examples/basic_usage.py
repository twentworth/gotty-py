#!/usr/bin/env python3
"""
Basic usage example for gotty-py client.

This example demonstrates how to connect to a gotty server and execute
commands.
"""

import os
import sys

# Add the parent directory to the path so we can import gotty_py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from gotty_client import GottyWebSocketClient


def main():
    """Main function demonstrating basic usage."""
    print("Gotty Python Client - Basic Usage Example")
    print("=" * 50)

    # Create client
    client = GottyWebSocketClient(
        webui_url="http://192.168.0.113:8222",
        username="admin",
        password="admin",
    )

    try:
        print("Connecting to gotty server...")
        if client.connect():
            print("✓ Connected successfully!")

            # Execute a simple command
            print("\nExecuting 'ls' command...")
            response = client.execute_command("ls", timeout=5.0)

            if response.success:
                print("✓ Command executed successfully!")
                print(f"Response: {response.data}")
            else:
                print(f"✗ Command failed: " f"{response.message}")

            # Get terminal output
            print("\nGetting terminal output...")
            output = client.get_terminal_output(last_n_lines=5)
            print(f"Last 5 lines: {output}")

            # Get command history
            print("\nGetting command history...")
            history = client.get_command_history()
            print(f"Command history: {history}")

        else:
            print("✗ Failed to connect to gotty server")
            return 1

    except Exception as e:
        print(f"✗ Error: {e}")
        return 1

    finally:
        print("\nClosing connection...")
        client.close()
        print("✓ Connection closed")

    print("\nExample completed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
