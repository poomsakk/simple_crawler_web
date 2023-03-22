import { useState } from "react";
import { Select, Space, Button } from "antd";
import { DownloadOutlined } from "@ant-design/icons";
import TableProvince from "./component/TableProvince";
import DropdownCollapse from "./component/DropdownCollapse";

function App() {
  const [selectProvince, setSelectProvince] = useState("Tak");
  const [loading, setLoading] = useState(false);

  const handleDownload = async () => {
    setLoading(true);
    try {
      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/${selectProvince}-csv`
      );
      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.style.display = "none";
      a.href = url;
      a.download = `${selectProvince}.csv`;
      document.body.appendChild(a);
      a.click();
      setLoading(false);
    } catch (error) {
      console.error(error);
      setLoading(false);
    }
  };

  return (
    <>
      <div className="container mx-auto mt-auto text-center">
        <div className="grid grid-cols-1 md:grid-cols-3 px-10 sm:px-15 md:px-20 lg:px-44 xl:px-72 pt-12 gap-4 content-center justify-center">
          <h2>เลือกจังหวัดที่จะแสดงรายชื่อวัด</h2>
          <Select
            defaultValue={selectProvince}
            onChange={(e) => setSelectProvince(e)}
            options={[
              { value: "Tak", label: "Tak (ตาก)" },
              { value: "Nakhon_Nayok", label: "Nakhon Nayok (นครนายก)" },
              { value: "Nakhon_Prathom", label: "Nakhon Prathom (นครพนม)" },
              { value: "Nakhon_Phanom", label: "Nakhon Phanom (นครปฐม)" },
            ]}
          />
          <Button
            className="bg-[#1677ff]"
            type="primary"
            shape="round"
            icon={<DownloadOutlined />}
            size="large"
            loading={loading}
            onClick={handleDownload}
          >
            Download as CSV
          </Button>
        </div>
        <DropdownCollapse></DropdownCollapse>
        <TableProvince selectProvince={selectProvince} />
      </div>
    </>
  );
}

export default App;
