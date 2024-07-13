
![Logo](https://forumai.gitbook.io/~gitbook/image?url=https%3A%2F%2F2630327285-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FV0DU8Z2zdzgU0cdeQYjJ%252Ficon%252FfSqUiPXc6zkQi7MU2SF9%252Flogo2.png%3Falt%3Dmedia%26token%3D988f020f-5222-4815-85e8-be2e6cca80bb&width=32&dpr=2&quality=100&sign=ef7b7c5e&sv=1)


# Integrate Mixtral8x7B with Python SDK 

The ForumAI Python SDK offers Python developers straightforward integration with the Mixtral8x-7B model on the testnet. It simplifies the adoption of advanced AI within applications by leveraging decentralized technology without requiring extensive blockchain expertise.

This SDK aims to simplify the use of advanced AI technologies for Python developers, making it easier to implement complex AI solutions without extensive blockchain expertise.

.

## Prerequisites

- Install Python & pip :
    - Download Python from the official website: [Python.org](https://www.python.org/downloads/)
    - Run the installer and follow the steps to complete  the   installation.
    - Ensure pip is installed by running : 
    `pip --version ` or `pip3 --version` in the terminal.
    
  If not installed, follow the [pip installation.](https://pip.pypa.io/en/stable/installation/)

- sFuel Claiming : 

  To perform transactions, follow these steps to obtain sFuel:    
  1. Visit [sFuel Station](https://www.sfuelstation.com/).
  2. Paste or Connect your wallet.
  3. Claim your sFuel for use on the Titan AI Hub chain.


## Installation

**SDK Installation**

Install the Python SDK using pip:

```bash
  pip install forumaisdk
```
or using pip3.

```bash
  pip3 install forumaisdk
```


### Configuration

Environment Setup

Configure essential environment variables such as `PRIVATE_KEY` and `WALLET_ADDRESS` to facilitate secure transactions.
 - EVM Wallet (Metamask,etc)



## Running Tests

Open the terminal and start the Python shell by typing:

```bash
  python3
```

Copy and paste the following code into the Python shell. Replace `your_private_key_here` and `your_wallet_address` with your actual wallet's private key and address:

```bash
  from ModelMarketSDK.ModelMarket import Mixtral8x7BModelMarketTestnet

  # Initialize the model market with your credentials
  model_market = Mixtral8x7BModelMarketTestnet(
    "your_private_key_here",
    "your_public_key_here"
)
```
and press enter on Python Shell.

You should see the output `“Initialized!”` Then you are good to go to the final step.

***Send a Machine Learning Inference Request:***

Define your chat input. The default question is "What is 2+2?" for testing. You can replace "What is 2+2?" with your question:

```bash
  chat = [{"role": "system", "content": "You are a helpful assistant!"}, {"role": "user", "content": "What is 2+2?"}]
  response = model_market.generate(3000, chat)
  print(response)
```

Example Output :

![Capture](https://mirror.xyz/_next/image?url=https%3A%2F%2Fimages.mirror-media.xyz%2Fpublication-images%2F2y9WWWmBKmeA6yeyffcQz.png&w=1920&q=75)