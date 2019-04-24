# 1 in 12 people live near an active or potentially active volcano
... or do they? Maybe. Maybe not. So I have this National Geographic book called
"Vocano: Iceland's Inferno" which makes the (probably well researched) claim that
"About 1 in 12 of the world's population live around Earth's active or potentially
active volcanoes." While this statement is a great icebreaker, is it true? Probably. 
And my script agrees.

This is all assuming that the "scientific" statement "near" means in the danger zone
of an active or potentially active volcano, which I assumed to be a 50 mile radius. 

## Data
All of my city location/population data can be found at [simplemaps](https://simplemaps.com/data/world-cities)
and all of my volcano data was grabbed from [OSU's Volcano World](http://volcano.oregonstate.edu/volcano_table),
but a file has been provided anyway. 

Is the data good? I don't doubt the information, but the sample size is very low. 
Only about 30% of the world's population is located in free csv I downloaded containing 
~13000 cities. Also, only ~450 volcanoes are included in the file while I believe about
1500 have been found on land.

## Conclusion
I don't know, I'm not a volcanologist. Output has been provided in the `output.txt` file.
A sample is below. 
```
Total Cities 12893
Population Cities 11276
Total Population 2455391824
Total Volcanoes 426
Potchefstroom is near SP
Polokwane is near Nikko-Shirane
Thohoyandou is near Rasshua
Kapiri Mposhi is near Lereboleng
Bulawayo is near Asama
Atbasar is near Acamarachi
Atbasar is near Barrier
Atasu is near SP
Embi is near Coatepeque
Esil is near Ungaran
Shalqar is near Atitlán
...
North Charleston is near Alaid
Taylor Mill is near Udina
Happy Valley is near Dieng
Medford is near Cameroon
Forest Grove is near Iliniza
Cornelius is near Iliniza
Fairview is near Acamarachi
Fairview is near Fogo
Fairview is near Oraefajokull
Scappoose is near Kilimanjaro
Milwaukie is near Dieng
Talent is near Roundtop
Hillsboro is near Iliniza
593 cities are near a volcano
6.805617106265969 % of people live near an active or potentially active volcano
```

So... Is 6.8% about 1 in 12? I guess 6.8% and 8.3% are pretty close. But really 
6.8% is closer to 1 in 15. But the real question is, do *you* live near an 
active or potentially active volcano?