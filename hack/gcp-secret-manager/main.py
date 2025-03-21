#!/usr/bin/env python3
import click

from google.cloud import secretmanager

# Test Platform's project in GCP Secret Manager
project_id = "YOUR_PROJECT_ID"

@click.group()
def cli():
    """CLI tool to manage secrets in Google Secret Manager."""
    pass



@click.command()
def login():
    """Login command to authenticate the user."""
    click.echo("Login process here...")
    client = secretmanager.SecretManagerServiceClient()
    print("created client :)")

cli.add_command(login)

if __name__ == "__main__":
    cli()