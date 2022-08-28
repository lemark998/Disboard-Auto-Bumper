import os, discum, time, random

bot = discum.Client(token = os.getenv("TOKEN") , log=False)
from discum.utils.slash import SlashCommander
    


from discum.utils.slash import SlashCommander

x=True

while x:
    def slashCommandTest(resp, guildID, channelID, botID):
        if resp.event.ready_supplemental:
            bot.gateway.request.searchSlashCommands(guildID, limit=10, query="bump") #query slash cmds
        if resp.event.guild_application_commands_updated:
            bot.gateway.removeCommand(slashCommandTest) #because 2 guild_app_cmd_update events are received...idk ask discord why
            slashCmds = resp.parsed.auto()['application_commands'] #get the slash cmds
            s = SlashCommander(slashCmds, application_id=botID) #for easy slash cmd data creation
            data = s.get(['bump'], inputs={'name':'test'})
            mes=bot.triggerSlashCommand(str(botID), channelID=channelID, guildID=guildID, data=data, sessionID=bot.gateway.session_id) #and send it off
            print('command send')
            print(mes)
            bot.gateway.close() #optional. It's better to remove this line actually.

    guildID = "1008490671000268940"
    channelID = "1008574078598262865"
    botID = "302050872383242240"
    bot.gateway.command(
        {
             "function": slashCommandTest,
             "params": {"guildID": guildID, "channelID": channelID, "botID": botID},
        }
    )
    bot.gateway.run()
    time.sleep(random.randint(14400, 15000))



        
