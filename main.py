import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url 
            await file.save(f'./{file_name}')
            await ctx.send (f'file telah disimpan dengan nama {file_name}')
            hasil = get_class('keras_model.h5', 'labels.txt', file_name) 

            if hasil[0] == 'Pipa Besi\n' and hasil[1] >=0.7:
                await ctx.send('ini adalah Pipa besi')
                await ctx.send('Pipa besi adalah sebuah tabung yang terbuat dari baja atau besi cor, yang digunakan untuk mengalirkan cairan atau gas dari satu tempat ke tempat lainnya. Pipa besi memiliki berbagai ukuran dan ketebalan dinding tergantung pada kebutuhan aplikasinya. Mereka dapat digunakan dalam berbagai industri seperti perminyakan, gas, air minum, perpipaan rumah tangga, sistem perpipaan industri, dan banyak lagi.')
            elif hasil[0] == 'Besi Kotak\n' and hasil[1] >=0.7:
                await ctx.send('ini adalah Besi kotak')
                await ctx.send('Besi kotak, juga dikenal sebagai hollow section atau square hollow section (SHS), adalah produk baja berbentuk kotak yang digunakan dalam berbagai aplikasi konstruksi. Mereka terbuat dari lembaran baja yang ditekuk menjadi bentuk kotak dengan sisi yang sama panjang di setiap sisi. Besi kotak sering digunakan sebagai bahan struktural dalam pembuatan bangunan, konstruksi jembatan, pagar, rangka kendaraan, dan berbagai aplikasi konstruksi lainnya.') 
            else:
                  await ctx.send('Gak Ada')   
    else:
        await ctx.send('gaada file yang diterima')

bot.run("MTE1ODM4ODUwMDcwNjYzNTgyNg.Gdiycn._7KaONAI12nvbHri6b9yop0ZxBhzHL68BVK_4M")
