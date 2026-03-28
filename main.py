import os
import logging
import json
import requests as req
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from flask import Flask
from threading import Thread

logging.basicConfig(level=logging.INFO)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GROQ_API_KEY = os.environ.get("GEMINI_API_KEY")
MAKE_WEBHOOK = "https://hook.eu1.make.com/bldhpbofq3tq4wzwplv8jr3c5s9j4tql"

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

async def generate(prompt):
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": prompt}]
        }
        r = req.post(url, headers=headers, json=data)
        return r.json()["choices"][0]["message"]["content"][:4000]
    except Exception as e:
        return f"Error: {str(e)}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
👑 EMPIRE BOT ONLINE

CONTENT COMMANDS:
/youtube - YouTube script
/tweet - 5 viral tweets
/instagram - 7 IG posts
/tiktok - TikTok script
/newsletter - Newsletter issue
/blog - SEO blog article
/podcast - Podcast script
/pinterest - 10 pin descriptions
/reddit - Reddit post
/medium - Medium article

MONEY COMMANDS:
/coldsequence - 5 email sales sequence
/salespage - Full sales page copy
/linkedinprofile - Optimized LinkedIn profile
/contentpackage - Full month content plan
/businessplan - Basic business plan
/adcopy - Facebook and Google ad copy
/resume - Professional resume
/pitch - Client pitch script
/productidea - Digital product idea
/pricingstrategy - Pricing strategy

OUTREACH COMMANDS:
/sendemail - Write AND send cold email automatically
/followup - Follow up email
/dmemail - DM script
/linkedinmsg - LinkedIn message
/proposal - Full client proposal

DAILY COMMANDS:
/report - Daily empire report
/tasks - Today's money tasks
/ask - Ask me anything
""")

async def youtube(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing YouTube script...")
    topic = " ".join(context.args) if context.args else "Top 5 AI tools that make money in 2025"
    prompt = f"Write a complete faceless YouTube video script about: {topic}. Include attention grabbing hook in first 10 seconds, main content with 5 points, and strong call to action. Make it 600 words and very engaging."
    result = await generate(prompt)
    await update.message.reply_text(f"📺 YouTube Script:\n\n{result}")

async def tweet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing tweets...")
    topic = " ".join(context.args) if context.args else "making money with AI"
    prompt = f"Write 5 viral tweets about {topic}. Each under 280 characters. Make them punchy with hooks. Number 1-5."
    result = await generate(prompt)
    await update.message.reply_text(f"🐦 Tweets:\n\n{result}")

async def instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing Instagram posts...")
    niche = " ".join(context.args) if context.args else "money and AI mindset"
    prompt = f"Write 7 Instagram posts for a {niche} page. Each post needs a strong first line hook, caption body, and 15 hashtags."
    result = await generate(prompt)
    await update.message.reply_text(f"📸 Instagram Posts:\n\n{result}")

async def tiktok(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing TikTok script...")
    topic = " ".join(context.args) if context.args else "how AI can make you money while you sleep"
    prompt = f"Write a 45 second viral TikTok script about {topic}. Hook in first 2 seconds. Fast paced. Add text overlay instructions."
    result = await generate(prompt)
    await update.message.reply_text(f"🎵 TikTok Script:\n\n{result}")

async def newsletter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing newsletter...")
    topic = " ".join(context.args) if context.args else "AI tools and passive income"
    prompt = f"Write a weekly newsletter about {topic}. Include catchy subject line, intro, 3 value sections, tool recommendation, and call to action. 500 words."
    result = await generate(prompt)
    await update.message.reply_text(f"📰 Newsletter:\n\n{result}")

async def blog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing blog article...")
    topic = " ".join(context.args) if context.args else "how to make money with AI in 2025"
    prompt = f"Write a full SEO blog article about {topic}. Include SEO title, meta description, introduction, 5 sections with headings, conclusion. 1000 words."
    result = await generate(prompt)
    await update.message.reply_text(f"📝 Blog Article:\n\n{result}")

async def podcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing podcast script...")
    topic = " ".join(context.args) if context.args else "making money online with AI tools"
    prompt = f"Write a 10 minute podcast script about {topic}. Include intro, 4 main talking points, sponsor break placeholder, and outro."
    result = await generate(prompt)
    await update.message.reply_text(f"🎙️ Podcast Script:\n\n{result}")

async def pinterest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing Pinterest pins...")
    niche = " ".join(context.args) if context.args else "make money online"
    prompt = f"Write 10 Pinterest pin descriptions for {niche} niche. Each needs title, 150 word description with keywords, and 5 hashtags."
    result = await generate(prompt)
    await update.message.reply_text(f"📌 Pinterest Pins:\n\n{result}")

async def reddit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing Reddit post...")
    topic = " ".join(context.args) if context.args else "how I make money with AI"
    prompt = f"Write an authentic Reddit post about {topic}. Include a story, specific details, lessons learned, invite discussion. 400 words. No promotional language."
    result = await generate(prompt)
    await update.message.reply_text(f"👽 Reddit Post:\n\n{result}")

async def medium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing Medium article...")
    topic = " ".join(context.args) if context.args else "how AI changed how I make money"
    prompt = f"Write a Medium article about {topic}. Personal story format. Hook, backstory, turning point, lessons, actionable advice. 800 words first person."
    result = await generate(prompt)
    await update.message.reply_text(f"✍️ Medium Article:\n\n{result}")

async def coldsequence(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing 5 email cold sequence...")
    service = " ".join(context.args) if context.args else "AI content writing service for small businesses"
    prompt = f"Write a 5 email cold outreach sequence selling {service}. Email 1 introduction, Email 2 follow up, Email 3 pain point, Email 4 case study, Email 5 final offer. Each max 150 words. Include subject lines."
    result = await generate(prompt)
    await update.message.reply_text(f"📧 Cold Email Sequence:\n\n{result}")

async def salespage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing full sales page...")
    product = " ".join(context.args) if context.args else "AI content writing service"
    prompt = f"Write a complete sales page for {product}. Include headline, problem section, solution, benefits, social proof placeholders, pricing, FAQ, and CTA. 600 words."
    result = await generate(prompt)
    await update.message.reply_text(f"💰 Sales Page:\n\n{result}")

async def linkedinprofile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing LinkedIn profile...")
    role = " ".join(context.args) if context.args else "AI content creator and freelancer"
    prompt = f"Write a complete optimized LinkedIn profile for a {role}. Include headline, about section 300 words, 3 experience entries, skills list. Make it attract clients."
    result = await generate(prompt)
    await update.message.reply_text(f"💼 LinkedIn Profile:\n\n{result}")

async def contentpackage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing full month content package...")
    niche = " ".join(context.args) if context.args else "AI and online business"
    prompt = f"Create a full 30 day content calendar for {niche}. Each week include 3 Instagram posts, 5 tweets, 1 YouTube idea, 1 blog topic, 1 newsletter topic. Professional format."
    result = await generate(prompt)
    await update.message.reply_text(f"📅 Monthly Content Package:\n\n{result}")

async def businessplan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing business plan...")
    business = " ".join(context.args) if context.args else "AI content agency"
    prompt = f"Write a concise business plan for a {business}. Include executive summary, target market, revenue model, pricing, marketing plan, 90 day action plan, financial projections."
    result = await generate(prompt)
    await update.message.reply_text(f"📊 Business Plan:\n\n{result}")

async def adcopy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing ad copy...")
    product = " ".join(context.args) if context.args else "AI content writing service"
    prompt = f"Write Facebook and Google ad copy for {product}. Include 3 Facebook ad variations with headline body and CTA. 3 Google search ads. 2 Instagram captions. All optimized for conversions."
    result = await generate(prompt)
    await update.message.reply_text(f"📣 Ad Copy:\n\n{result}")

async def resume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing resume...")
    role = " ".join(context.args) if context.args else "digital marketer and content creator"
    prompt = f"Write a professional ATS optimized resume for a {role}. Include summary, skills, 3 work experience entries with bullet points, education. Clean format."
    result = await generate(prompt)
    await update.message.reply_text(f"📄 Resume:\n\n{result}")

async def pitch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing pitch...")
    service = " ".join(context.args) if context.args else "AI content writing service"
    prompt = f"Write a 60 second verbal pitch and 3 paragraph written pitch for {service}. Include problem, solution, unique value, social proof placeholder, call to action."
    result = await generate(prompt)
    await update.message.reply_text(f"🎯 Pitch:\n\n{result}")

async def productidea(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Generating product ideas...")
    niche = " ".join(context.args) if context.args else "productivity and AI"
    prompt = f"Generate 3 digital product ideas for {niche}. For each include product name, description, how to create with AI, where to sell, price, estimated monthly revenue."
    result = await generate(prompt)
    await update.message.reply_text(f"💡 Product Ideas:\n\n{result}")

async def pricingstrategy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Building pricing strategy...")
    service = " ".join(context.args) if context.args else "freelance AI content writing"
    prompt = f"Create a complete pricing strategy for {service}. Include starter, professional, premium packages with prices. How to upsell, handle objections, and a pricing page template."
    result = await generate(prompt)
    await update.message.reply_text(f"💲 Pricing Strategy:\n\n{result}")

async def sendemail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing and sending email automatically...")
    niche = " ".join(context.args) if context.args else "small business owners"
    prompt = f"Write a cold outreach email to {niche} offering AI content writing services. Return ONLY a raw JSON object with exactly these 3 keys: to, subject, body. No explanation, no markdown, just the JSON."
    result = await generate(prompt)
    try:
        data = json.loads(result)
        req.post(MAKE_WEBHOOK, json=data)
        await update.message.reply_text(f"✅ Email SENT automatically!\n\nTo: {data['to']}\nSubject: {data['subject']}\n\nBody preview:\n{data['body'][:200]}...")
    except:
        await update.message.reply_text(f"📧 Email drafted:\n\n{result}")

async def followup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing follow up...")
    context_text = " ".join(context.args) if context.args else "sent cold email about content writing 3 days ago no reply"
    prompt = f"Write a follow up email for: {context_text}. Short, add value, not pushy, different angle. Max 100 words. Include subject line."
    result = await generate(prompt)
    await update.message.reply_text(f"📨 Follow Up:\n\n{result}")

async def dmemail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing DM script...")
    platform = " ".join(context.args) if context.args else "Instagram business owner"
    prompt = f"Write a DM outreach script for {platform}. Opener referencing their content, genuine compliment, problem noticed, your solution, soft CTA. Max 80 words. Natural not salesy."
    result = await generate(prompt)
    await update.message.reply_text(f"💬 DM Script:\n\n{result}")

async def linkedinmsg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing LinkedIn message...")
    target = " ".join(context.args) if context.args else "marketing manager at a small business"
    prompt = f"Write a LinkedIn connection request and follow up message for a {target}. Connection request max 300 chars. Follow up max 150 words. Professional and value focused."
    result = await generate(prompt)
    await update.message.reply_text(f"💼 LinkedIn Messages:\n\n{result}")

async def proposal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Writing proposal...")
    project = " ".join(context.args) if context.args else "monthly content creation for a small business"
    prompt = f"Write a professional client proposal for {project}. Include project overview, scope, deliverables, timeline, pricing table, terms, next steps. Ready to send."
    result = await generate(prompt)
    await update.message.reply_text(f"📋 Proposal:\n\n{result}")

async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
📊 EMPIRE DAILY REPORT

🌅 CONTENT TASKS:
/youtube - Create video script
/tweet - Post 5 tweets
/instagram - Schedule 7 posts
/tiktok - Create 3 videos
/newsletter - Send weekly issue
/blog - Publish 1 article
/pinterest - Post 10 pins
/reddit - Post 1 value post
/medium - Publish 1 article

💰 MONEY TASKS:
/coldsequence - Send to 5 prospects
/salespage - Create for your service
/linkedinprofile - Optimize today
/contentpackage - Sell to 1 client
/adcopy - Run 1 ad

📧 OUTREACH TASKS:
/sendemail - Auto send 10 cold emails
/followup - Follow up yesterday leads
/dmemail - DM 10 people
/linkedinmsg - Connect with 20 people
/proposal - Send to warm leads

🔥 FOCUS: Type /sendemail restaurant owners
""")

async def tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
✅ TODAY'S $100 TASKS

MORNING:
1. /sendemail restaurant owners
2. /sendemail salon owners
3. /sendemail gym owners
4. /linkedinmsg marketing managers

AFTERNOON:
5. /tweet make money with AI
6. /instagram money mindset
7. /blog how AI helps small business

EVENING:
9. /followup
10. /proposal for anyone who replied

💡 ONE CLIENT = $50-150
THREE CLIENTS = $100+ DAY
""")

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args) if context.args else "give me the best money making tip for today"
    await update.message.reply_text("⏳ Thinking...")
    result = await generate(question)
    await update.message.reply_text(f"🤖 Answer:\n\n{result}")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    result = await generate(text)
    await update.message.reply_text(result)

def main():
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("youtube", youtube))
    application.add_handler(CommandHandler("tweet", tweet))
    application.add_handler(CommandHandler("instagram", instagram))
    application.add_handler(CommandHandler("tiktok", tiktok))
    application.add_handler(CommandHandler("newsletter", newsletter))
    application.add_handler(CommandHandler("blog", blog))
    application.add_handler(CommandHandler("podcast", podcast))
    application.add_handler(CommandHandler("pinterest", pinterest))
    application.add_handler(CommandHandler("reddit", reddit))
    application.add_handler(CommandHandler("medium", medium))
    application.add_handler(CommandHandler("coldsequence", coldsequence))
    application.add_handler(CommandHandler("salespage", salespage))
    application.add_handler(CommandHandler("linkedinprofile", linkedinprofile))
    application.add_handler(CommandHandler("contentpackage", contentpackage))
    application.add_handler(CommandHandler("businessplan", businessplan))
    application.add_handler(CommandHandler("adcopy", adcopy))
    application.add_handler(CommandHandler("resume", resume))
    application.add_handler(CommandHandler("pitch", pitch))
    application.add_handler(CommandHandler("productidea", productidea))
    application.add_handler(CommandHandler("pricingstrategy", pricingstrategy))
    application.add_handler(CommandHandler("sendemail", sendemail))
    application.add_handler(CommandHandler("followup", followup))
    application.add_handler(CommandHandler("dmemail", dmemail))
    application.add_handler(CommandHandler("linkedinmsg", linkedinmsg))
    application.add_handler(CommandHandler("proposal", proposal))
    application.add_handler(CommandHandler("report", report))
    application.add_handler(CommandHandler("tasks", tasks))
    application.add_handler(CommandHandler("ask", ask))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == "__main__":
    main()
