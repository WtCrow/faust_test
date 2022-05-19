#Faust agent communication

Open 2 terminal and enter next commands:
- `faust -A consumer worker -l info -p 6666`
- `faust -A producer worker -l info -p 6667`

After starting workers, open 3 terminal and enter:
- `faust -A producer send @producer_agent "Hello Faust"`
