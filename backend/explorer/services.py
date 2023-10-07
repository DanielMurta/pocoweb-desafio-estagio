def process_data_challenge1(opunits, oilfields, wells):
    """
    Função que processa os dados para estrutura solicitada
    """
    # TODO: Escreva seu código aqui.
    result = []

    for opunit in opunits:
        result.append([["opunit/{}".format(opunit.id)]])

    for oilfield in oilfields:
        opunit_id = oilfield.operational_unit.id
        result.append([["opunit/{}".format(opunit_id)], ["oilfield/{}".format(oilfield.id)]])

    for well in wells:
        oilfield_id = well.oilfield.id
        opunit_id = well.oilfield.operational_unit.id
        result.append([["opunit/{}".format(opunit_id)], ["oilfield/{}".format(oilfield_id)], ["well/{}".format(well.id)]])

    return result

def process_data_challenge2(opunits, oilfields, wells):
    """
    Função que processa os dados para estrutura solicitada
    """
    # TODO: Escreva seu código aqui
    def create_oilfield_node(oilfield, wells):
            oilfield_node = {
                "id": oilfield.id,
                "name": oilfield.name,
            }
            if wells:
                oilfield_node["children"] = [create_well_node(well) for well in wells]
            return oilfield_node

    def create_well_node(well):
        return {
            "id": well.id,
            "name": well.name,
        }

    def create_opunit_node(opunit, oilfields):
        opunit_node = {
            "id": opunit.id,
            "name": opunit.name,
        }
        if oilfields:
            opunit_node["children"] = [create_oilfield_node(oilfield, wells.filter(oilfield=oilfield)) for oilfield in oilfields]
        return opunit_node

    result = [create_opunit_node(opunit, oilfields.filter(operational_unit=opunit)) for opunit in opunits]

    return result

