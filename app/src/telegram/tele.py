from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from src.settings import base_settings

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! To track a product, please provide the product link.",
    )
    context.user_data["state"] = "waiting_for_product_link"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_state = context.user_data.get("state")

    if user_state == "waiting_for_product_link":
        user_product_link = update.message.text
        context.user_data["product_link"] = user_product_link
        context.user_data["state"] = "waiting_for_price"

        await update.message.reply_text(
            "Got it! Now, please enter your expected price for this product."
        )

    elif user_state == "waiting_for_price":
        try:
            user_price = float(update.message.text)
            context.user_data["expected_price"] = user_price
            context.user_data["state"] = None 

            product_link = context.user_data.get("product_link")
            await update.message.reply_text(
                f"Thank you! I will now track the product: {product_link} at the expected price of ₹{user_price:.2f}."
            )
        except ValueError:
            await update.message.reply_text("Invalid price! Please enter a valid number.")

    else:
        await update.message.reply_text(
            "I'm not sure what you're trying to do. Type /start to begin tracking a product."
        )

def main() -> None:
    application = Application.builder().token(f"{base_settings.bot_token}").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()
