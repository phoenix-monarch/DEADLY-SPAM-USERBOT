FROM sandy1709/catuserbot:alpine

#clonning repo 
RUN git clone https://github.com/DEADLY-FIGHTERS/DEADLY_SPAM_BOT.git /root/DeadlyOp
#working directory 
WORKDIR /root/DeadlyOp

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/DeadlyOp/bin:$PATH"

CMD ["python3","-m","DeadlyOp"]
