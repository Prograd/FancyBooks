# FancyBooks

This is one of my projects that I'm currently working on. **It's still in progress**. The backend part is almost completed, but there are still a few issues that needs to be done.
The frontend part is at the very beginning of the development. The project is more like a proof of concept. I wanted to test how this mix of technologies will work together.

**Base branch:** master

**Frontend feature branch:** feature/add-frontend-layer

## Technical stack: 

- Django
- GraphQL
- Gatsbyjs

## Bussness context

Create a shop with diffrent books as a products. We should be allowed to change products through Django admin pannel and also see products on frontend layer. 
Moreover we should be allowed to create an client account and save a list of products which we would like to buy.

## Architecture explanation

Frontend side will fetch data about products thrugh GraphQL API which is provided by Django. 
This data won't be static but I' gonna use the static capabilities of gatsby to render pages like about and other which will be needed.
