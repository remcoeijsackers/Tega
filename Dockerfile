# Use an official Python runtime as a parent image
FROM python:3.13-rc-bookworm

ADD requirements.txt /requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9000

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set the working directory to /app
WORKDIR /code

# Copy the current directory contents into the container at /app

COPY . /code

# Define environment variable
#ENV FLASK_APP app

# Run app.py when the container launches

CMD ["python", "-m", "flask", "run", "--port", "9000","--host", "0.0.0.0", "--debug"]

#CMD ["python", "-m", "flask", "--app", "src/app", "run", "--port", "9000", "--debug"]
