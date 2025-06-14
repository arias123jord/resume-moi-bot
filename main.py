python
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler

BOT_TOKEN = '7978605117:AAHIrRbcE9S712u8qJYXkUJvYyAON0WsRmc'  # Remplace ceci par ton token Telegram

user_usage = {}

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 Bienvenue sur Resume_Moi !\n\nEnvoie-moi un texte ou un titre de livre, je te résume ça.\nTu as droit à 3 résumés gratuits.")

def simulate_resume(text):
    return f"📝 Résumé : Ce texte parle probablement de '{text[:30]}...' (résumé simulé)."

def handle_message(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user_usage[user_id] = user_usage.get(user_id, 0)

    if user_usage[user_id] < 3:
        user_usage[user_id] += 1
        text = update.message.text
        summary = simulate_resume(text)
update.message.reply_text(summary + f"\n\nUtilisation : {user_usage[user_id]}/3")
    else:
        button = InlineKeyboardButton("✅ J’ai payé", callback_data="paid")
        markup = InlineKeyboardMarkup([[button]])
        update.message.reply_text(
            "🚫 Tu as atteint ta limite gratuite de 3 résumés.\n\n💰 Pour débloquer l’accès illimité :\n- Binance Pay : tonemail@domaine.com\n- MTN : 99 XX XX XX\n\nClique sur « J’ai payé » après paiement.",
            reply_markup=markup
        )

def handle_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    user_id = query.from_user.id
    user_usage[user_id] = 0
    query.edit_message_text("✅ Paiement confirmé. Tu peux reprendre tes résumés. Merci !")

if _name_ == '_main_':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(handle_callback))
    print("Bot lancé.")
    app.run_polling()
```
