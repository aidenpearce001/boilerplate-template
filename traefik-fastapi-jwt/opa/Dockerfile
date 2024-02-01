FROM openpolicyagent/opa:latest

# Set the working directory
WORKDIR /opa

# Copy your policy files
COPY ./policies/*.rego /opa/policies/

EXPOSE 8181

CMD ["run", "--log-level=debug", "--server", "/opa/policies"]