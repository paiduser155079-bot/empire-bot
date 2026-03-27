import os
import asyncio
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai
from flask import Flask
from threading import Thread

logging.basicConfig(level=logging.INFO)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
OWNER_ID = os.environ.get("OWNER_ID")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
👑 EMPIRE BOT ONLINE

Your commands:
/youtube - Generate YouTube script
/tweet - Generate 5 tweets
/email - Write outreach email
/resume - Rewrite a resume
/instagram - Generate 7 posts
/tiktok - Generate TikTok script
/newsletter - Write newsletter
/blog - Write blog article
/pitch - Write client pitch
/product - Create digital product idea
/report - Daily empire report
/ask - Ask me anything
""")

async def youtube(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Generating YouTube script...")
    topic = " ".join(context.args) if context.args else "Top 5 AI tools that make money"
    prompt = f"Write a complete faceless YouTube video script about: {topic}. Include hook, main content, and call to action. Make it engaging and 500 words."
    response = model.generate_content(prompt)
    await update.message.reply_text(f"📺 YouTube Script:\n\n{response.text[:3000]}")

async def tweet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Generating tweets...")
    topic = " ".join(context.args) if context.args else "making money with AI"
    prompt = f"Write 5 viral tweets about {topic}. Each tweet should be under 280 characters. Make them engaging with hooks. Number them 1-5."
    response = model.generate_content(prompt)
    await update.message.reply_text(f"🐦 Tweets:\n\n{response.text[:3000]}")

async def email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing outreach email...")
    niche = " ".join(context.args) if context.args else "small business owners"
    prompt = f"Write a cold outreach email to {niche} offering AI content writing services. Keep it short, friendly, and with a clear call to action. Make it feel personal not spammy."
    response = model.generate_content(prompt)
    await update.message.reply_text(f"📧 Email:\n\n{response.text[:3000]}")

async def resume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Creating resume template...")
    role = " ".join(context.args) if context.args else "software developer"
    prompt = f"Write a professional ATS-optimized resume template for a {role}. Include summary, skills, experience section with bullet points, and education. Make it impressive."
    response = model.generate_content(prompt)
    await update.message.reply_text(f"📄 Resume:\n\n{response.text[:3000]}")

async def instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Generating Instagram posts...")
    niche = " ".join(context.args) if context.args else "motivation and money mindset"
    prompt = f"Write 7 Instagram posts for a {niche} page. Each post should have a caption and 10 relevant hashtags. Make them engaging and shareable."
    response = model.generate_content(prompt)
    await update.message.reply_text(f"📸 Instagram Posts:\n\n{response.text[:3000]}")

async def tiktok(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing TikTok script...")
    topic = " ".join(context.args) if context.args else "how to make money online with AI"
    prompt = f"Write a 30 second viral TikTok script about {topic}. Include hook in first 3 seconds, fast paced content, and strong ending. Add text overlay suggestions."
    response = model.generate_content(prompt)
    await update.message.reply_text(f"🎵 TikTok Script:\n\n{response.text[:3000]}")

async def newsletter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing newsletter...")
    topic = " ".join(context.args) if context.args else "AI tools and making money online"
    prompt = f"Write a weekly newsletter issue about {topic}. Include intro, 3 main sections with value, and a call to action. Keep it engaging and under 600 words."
    response = model.generate_content(prompt)
    await update.message.reply_text(f"📰 Newsletter:\n\n{response.text[:3000]}")

async def blog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing blog article...")
    topic = " ".join(context.args) if context.args else "how to make money with AI in 2025"
    prompt = f"Write an SEO optimized blog article about {topic}. Include title, meta description, introduction, 4 main sections with subheadings, and conclusion. 800 words."
    response = model.generate_content(prompt)
    await update.message.reply_text(f"📝 Blog:\n\n{response.text[:3000]}")

async def pitch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing pitch...")
    service = " ".join(context.args) if context.args else "AI content writing service"
    prompt = f"Write a short compelling sales pitch for a {service}. Target small business owners. Include problem, solution, price suggestion, and call to action. Keep under 200 words."
    response = model.generate_content(prompt)
    await update.message.reply_text(f"💼 Pitch:\n\n{response.text[:3000]}")

async def product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Creating product idea...")
    niche = " ".join(context.args) if context.args else "productivity and AI"
    prompt = f"Create a digital product idea for {niche} niche. Include product name, description, what it contains, suggested price, and how to sell it. Make it something that can be created with AI."
    response = model.generate_content(prompt)
    await update.message.reply_text(f"🛒 Product Idea:\n\n{response.text[:3000]}")

async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
📊 EMPIRE DAILY REPORT

🌅 Today's Tasks:
/youtube - Create video script
/tweet - Post 5 tweets
/email - Send 10 outreach emails
/instagram - Schedule 7 posts
/tiktok - Create 3 videos
/newsletter - Send weekly issue
/blog - Publish 1 article
/pitch - Send 5 pitches
/product - List 1 new product

💡 Tip of the day:
Focus on outreach first — fastest money.
Send 10 emails today using /email

🔥 Your empire is running. Keep going.
""")

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args) if context.args else "give me one money making tip"
    await update.message.reply_text("⏳ Thinking...")
    response = model.generate_content(question)
    await update.message.reply_text(f"🤖 Answer:\n\n{response.text[:3000]}")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    response = model.generate_content(text)
    await update.message.reply_text(response.text[:3000])

def main():
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("youtube", youtube))
    application.add_handler(CommandHandler("tweet", tweet))
    application.add_handler(CommandHandler("email", email))
    application.add_handler(CommandHandler("resume", resume))
    application.add_handler(CommandHandler("instagram", instagram))
    application.add_handler(CommandHandler("tiktok", tiktok))
    application.add_handler(CommandHandler("newsletter", newsletter))
    application.add_handler(CommandHandler("blog", blog))
    application.add_handler(CommandHandler("pitch", pitch))
    application.add_handler(CommandHandler("product", product))
    application.add_handler(CommandHandler("report", report))
    application.add_handler(CommandHandler("ask", ask))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()
