all: _get_latest_source _update_virtualenv 

REPO_URL := https://github.com/phelukas/TDD
BASE_DRI := ./scripts

_get_latest_source: 
	@$(BASE_DRI)/_get_latest_source.sh

_update_virtualenv:
	@$(BASE_DRI)/_update_virtualenv.sh


# criar depois quando projeto tiver mais estruturado
# NÃO ESQUECER DE POR LA EM CIMA NO ALL
# _create_or_update_dotenv:
# 	@$(BASE_DRI)/_create_or_update_dotenv.sh

