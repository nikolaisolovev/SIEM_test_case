"""
Это событие начинается с даты и времени, затем идет "ksmg.loc KSMG:",
после чего следует описание и статус.
"""

first = r"^(.*?)\s+ksmg\.loc\s+KSMG:\s+(.*?)\s+all\s+messages\s+in\s+MTA\s+queues:\s+(.*?)"

regex_link_1 = 'https://regex101.com/r/o2dFXu/1'


"""
Это событие начинается с приоритета, даты и времени, 
затем идет название устройства и подробности события.
"""

second = r"<(\d+)>(\w+\s+\d+\s+\d+\s+\d+:\d+:\d+)\s+(\w+)\s+%%\d+\w+/\d+/\w+\((\w+)\)\[(\d+)\]:(.*)"

regex_link_2 = 'https://regex101.com/r/JhWbse/1'


"""
Это событие начинается с даты и времени, затем идет "HMC:", 
и затем подробности о неудачной попытке создания логической партиции.
"""

third = r"(.*?)\s+HMC:\s+(.*?\sfailed\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+)$"

regex_link_3 = 'https://regex101.com/r/cqamDi/1'


"""
Это событие начинается с даты, времени и временной зоны, 
затем следует информация об аутентификации, успешности доступа и другие детали.
"""

fourth = r"^(.*?)\s+(\d+:\d+:\d+)\s+MSK,\d+,\d+,(.*?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?)$"

regex_link_= 'https://regex101.com/r/B65H6H/1'
