from ModelMarketSDK.ModelMarket import Mixtral8x7BModelMarketTestnet

# Initialize the model market with your credentials
model_market = Mixtral8x7BModelMarketTestnet(
    "PRIVATE_KEY",
    "WALLET_ADDRESS"
)



#Machine Learning Inference Request
chat = [{"role": "system", "content": "You are a helpful assistant!"}, {"role": "user", "content": "What is 30+1070?"}]
response = model_market.generate(3000, chat)
print(response)

