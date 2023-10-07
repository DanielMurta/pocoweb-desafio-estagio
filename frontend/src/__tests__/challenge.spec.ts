import { expect, test } from "vitest";
import { processData } from "../utils/challenge";
import { OilfieldType, OperationalUnitType, WellType } from "../@types/domain";
import { DataNode } from "antd/es/tree";

test("Test processedData functions", () => {
  const opunits: OperationalUnitType[] = [
    { id: 1, name: "Unidade operacional 1" },
  ];
  const oilfields: OilfieldType[] = [
    { id: 1, name: "Campo 1", operational_unit: "1" },
  ];
  const wells: WellType[] = [
    { id: 1, name: "Poço 1", oilfield: "1" },
  ];

  const result: DataNode[] = [
    {
      title: "Unidade operacional 1",
      key: "opunit-1",
      children: [
        {
          title: "Campo 1",
          key: "oilfield-1",
          children: [
            { title: "Poço 1", key: "well-1" },
          ],
        },
      ],
    },
  ];
  
  expect(processData(opunits, oilfields, wells)).deep.equal(result);
});
