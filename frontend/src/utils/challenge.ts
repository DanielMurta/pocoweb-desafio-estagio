import { DataNode } from "antd/es/tree";
import { OilfieldType, OperationalUnitType, WellType } from "../@types/domain";

/**
 * Função que processa os dados para o formato solicitado
 */
export function processData(
  opunits: OperationalUnitType[],
  oilfields: OilfieldType[],
  wells: WellType[]
) {
  console.log("processData", {
    opunits,
    oilfields,
    wells,
  });
  const result: DataNode[] = [];

  opunits.forEach((opunit) => {
    const opunitNode: DataNode = {
      title: opunit.name,
      key: `opunit-${opunit.id}`,
    };

    const oilfieldsInOpunit = oilfields.filter(
      (oilfield) => oilfield.operational_unit === opunit.id.toString()
    );

    const oilfieldNodes: DataNode[] = oilfieldsInOpunit.map((oilfield) => {
      const oilfieldNode: DataNode = {
        title: oilfield.name,
        key: `oilfield-${oilfield.id}`,
      };

      const wellsInOilfield = wells.filter(
        (well) => well.oilfield === oilfield.id.toString()
      );

      const wellNodes: DataNode[] = wellsInOilfield.map((well) => ({
        title: well.name,
        key: `well-${well.id}`,
      }));

      if (wellNodes.length > 0) {
        oilfieldNode.children = wellNodes;
      }

      return oilfieldNode;
    });

    if (oilfieldNodes.length > 0) {
      opunitNode.children = oilfieldNodes;
    }

    result.push(opunitNode);
  });

  return result;
}
