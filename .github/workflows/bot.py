name: Run Telegram Bot

on:
  push:
    branches: [main]

jobs:
  bot:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.12"
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run Bot
        env:
          BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
          ADMIN_ID: ${{ secrets.ADMIN_ID }}
        run: python bot.py
