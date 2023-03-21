import React, { useState, useEffect } from "react";
import { Table } from "antd";
import type { ColumnsType } from "antd/es/table";

interface Iprops {
  selectProvince: string;
}

interface DataType {
  key: React.Key;
  number: number;
  name: string;
}

const columns: ColumnsType<DataType> = [
  {
    title: "NO.",
    dataIndex: "number",
    width: "20%",
  },
  {
    title: "Name",
    dataIndex: "name",
  },
];

const TableProvince: React.FC<Iprops> = (props) => {
  const dataOnTable: DataType[] = [];
  const [loadingTable, setLoadingTable] = useState(false);
  const [provinceDataArr, setProvinceData] = useState([]);

  for (let i = 0; i < provinceDataArr.length; i++) {
    dataOnTable.push({
      key: i,
      number: i + 1,
      name: provinceDataArr[i],
    });
  }

  useEffect(() => {
    const fetchData = async () => {
      setLoadingTable(true);
      console.log("x");
      try {
        const response = await fetch(
          `${import.meta.env.VITE_API_URL}/${props.selectProvince}-data`
        );
        const json = await response.json();
        setProvinceData(json);
        setLoadingTable(false);
      } catch (error) {
        console.error(error);
        setLoadingTable(false);
      }
    };

    fetchData();
  }, [props.selectProvince]);

  return (
    <>
      {loadingTable ? (
        <p>Loading...</p>
      ) : (
        <Table
          className="px-10"
          columns={columns}
          dataSource={dataOnTable}
          size="middle"
          pagination={{ position: ["bottomCenter"] }}
        />
      )}
    </>
  );
};

export default TableProvince;
