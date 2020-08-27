from domain.liste_de_lieux import liste_de_lieux


class Get:
    class Returns200:
        #@clean_database
        def when_list_show_types(self, app):
            # when
            response = {}

            # then
            response_json = response.json
            assert response.status_code == 200
            assert response_json == liste_de_lieux
