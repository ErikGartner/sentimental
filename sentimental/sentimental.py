from model import SentimentModel

model = SentimentModel()
model.train(['data/_ruhburg'])
print(model.sentiment('attackerad'))
print(model.sentiment('schysst'))
