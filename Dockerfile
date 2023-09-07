FROM amazon/aws-lambda-python:3.8

ENV LAMBDA_ROOT="/var/task"

RUN pip install pipenv==2022.9.24

COPY . /bot
WORKDIR /bot

RUN pipenv install --system --deploy --ignore-pipfile

# Grab the zappa handler.py and put it in the working directory
RUN ZAPPA_HANDLER_PATH=$( \
    python -c "from zappa import handler; print (handler.__file__)" \
    ) \
    && echo $ZAPPA_HANDLER_PATH \
    && cp $ZAPPA_HANDLER_PATH ${LAMBDA_ROOT}

CMD [ "handler.lambda_handler" ]
