# Azurite Showcase
A minimal example of how to emulate Azure Blob storage in your Python project during local development and CI.

This example illustrates using [azurite](https://github.com/Azure/Azurite) as storage emulator, [adlfs](https://github.com/Azure/Azurite) for interacting with azure cloud storage and [pytest](https://docs.pytest.org/en/latest/) as testing framework.

When you can use this setup?

* You're developing in a team and your Python application has to interact with Azure Blob Storage
* You want your setup to be identical for you're whole team
* You want to run all you're tests locally and in a CI pipeline
* You want to test custom io functionality
* You want your tests to be indenpendent of any actual cloud resource

## Resources
* [Blog post](https://blog.johnnyreilly.com/2021/05/15/azurite-and-table-storage-dev-container/) by [John Reilly](https://twitter.com/johnny_reilly) for the devcontainer setup
* [Azurite Repo](https://github.com/Azure/Azurite)

## Contact
Alexander Fottner a.fottner@googlemail.com
