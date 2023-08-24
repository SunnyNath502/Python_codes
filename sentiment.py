
from textblob import TextBlob

text='''Sony has revealed the PlayStation Plus monthly games lineup for August. There’s no clear headliner here, but a trio of nifty titles are about to drop, including the incredible Zelda-ish adventure Death’s Door and a little-known golf sim called PGA Tour 2K23. Also in the lineup is Media Molecule’s long-running game-making platform Dreams.

Dreams is a community-focused app that builds upon the level-creation tools first debuted in the LittleBigPlanet series. Players have used the system to make just about anything you can imagine, from VR experiences to full-fledged CGI movies. Sony even allowed some of the more popular creators to sell their works.

Unfortunately, Sony is winding down Dreams, as the company recently announced it will stop releasing updates later this year. The launch on PS Plus, however, will provide users with one last hurrah, especially given the final game on this month’s list of releases, which is another Media Molecule title. Tren is a train-based adventure game that was entirely built in Dreams and only accessible within the title. Sony calls it a “nostalgic adventure that puts you in the driving seat of a remarkable toy train, and tells a personal tale about growing up – and the transformative power of play."

These titles are all available on August 1st and you have until the final day of July to scoop up expiring games like Call of Duty: Black Ops Cold War, Alan Wake Remastered and Endling – Extinction is Forever.


Terms and Privacy Policy
Privacy Dashboard
About Our Ads

Sony's PlayStation Portal remote player is a $200 handheld just for PS5 game streaming
The company has revealed more about its first wireless earbuds for PS5 as well as another set of headphones.
Kris Holt
Kris Holt
Contributing Reporter
Wed, Aug 23, 2023, 7:37 PM GMT+5:30·3 min read


Sony Interactive Entertainment
Several months back, Sony teased a dedicated remote play device for the PlayStation 5 as well as new gaming earbuds. Now, the company has revealed more details about the device. It's called the PlayStation Portal remote player.

The handheld looks a bit like a tablet wedged between two halves of a DualSense controller. It can stream games from your PS5 console, so when someone else is using the TV or you're in another room (or even travelling), you can still play remotely via WiFi without having to use your phone, tablet or computer. Sony says the snappily named PlayStation Portal remote player has an eight-inch LCD screen that delivers 1080p visuals at 60 frames per second. The device also benefits from DualSense features such as haptic feedback and adaptive triggers.

There is a 3.5mm headphone jack too. That should come in handy as, according to IGN, there's no Bluetooth function. You'll either need to use Sony's new earbuds or headphones, or plug in a wired headset.

Perhaps unsurprisingly, there's no support for PS VR2 games. You'll still need to hook your headset up to your PS5 directly to play VR games. Unfortunately, Sony says cloud game streaming through PlayStation Plus Premium isn't supported either. You'll have to install a game on a PS5 to play it remotely on the PlayStation Portal. That's disappointing, especially considering that the company is testing the ability to stream PS5 games to the console.

In addition, you better hope your WiFi stays up. As IGN notes, the PlayStation Portal doesn't run any apps locally at all. Everything goes through your PS5 — you can watch movies and TV shows on the handheld via the console's media apps — so if your WiFi network's down, the PlayStation Portal will essentially be useless.

Streaming-focused handhelds such as the Razer Edge are able to run Android apps locally. You can use third-party devices such as that, the ASUS ROG Ally or a Steam Deck to play your PS5 remotely too.

The PlayStation Portal remote player will arrive later this year. It will cost $200 in the US, £200 in the UK, €220 in the rest of Europe and 29,980 Yen in Japan.

Sony's Pulse Explore earbuds and charging case.
Sony Interactive Entertainment
On top of that, Sony has revealed more about its first wireless earbuds for PS5 and the PlayStation Portal remote player, as well as new headphones it designed for both systems. It says the Pulse Explore earbuds and Pulse Elite headset both support low latency lossless audio from PS5 and the handheld thanks to its new PlayStation Link tech.

A USB adapter is needed to connect the earbuds and headphones to PS5 via PlayStation Link. The tech will also be supported on PC and Mac. The Pulse Explore earbuds and Pulse Elite include multipoint connectivity as well. You can connect them to both your PS5 and a Bluetooth device (such as your phone) simultaneously, so you can easily answer a call while playing a game.

The earbuds and headset also each have custom-designed planar magnetic drivers (the first PlayStation audio devices to include them). Sony claims that it's one of the first companies to offer consumer earbuds with this tech, which it says delivers "an audiophile-level listening experience normally found in premium headphones for professional sound engineers.
 '''
blob = TextBlob(text)
sentiment_score = blob.sentiment.polarity
sentiment_percent = ((sentiment_score + 1) / 2) * 100  # Convert to percentage
# if sentiment_score > 0:
#     sentiment = "Positive"
# elif sentiment_score < 0:
#     sentiment = "Negative"
# else:
#     sentiment = "Neutral"
print(sentiment_percent)
print('tested')