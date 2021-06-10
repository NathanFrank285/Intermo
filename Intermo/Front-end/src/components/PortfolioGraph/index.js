import React, { useEffect } from "react";
import { getUserBalanceThunk } from '../../store/userBalance';
import { useDispatch, useSelector } from "react-redux";
import { PieChart, Pie, Tooltip, ResponsiveContainer, Cell, Legend } from "recharts";
import './PortfolioGraph.css'

function PortfolioGraph() {
  const dispatch = useDispatch();
  const userBalance = useSelector((state) => state?.userBalance?.balances);

  useEffect(() => {
    dispatch(getUserBalanceThunk());
    // eslint-disable-next-line
  }, []);
  const COLORS = ["#018FFE", "#50514F", "#DFE0E2", "#F24C00", "#C1DF1F", "#679436"];

  const CustomTooltip = ({ active, payload, label }) => {
    if (active) {
      const base = payload[0].payload.currencyId.split("/")[0];

      return (
        <div className="custom-tooltip">
          <p className="label">{`${payload[0].payload.currencyId}`}</p>
          <p className="desc">{`You have ${payload[0].payload.quantity} ${base}'s`}</p>
        </div>
      );
    }

    return null;
  };

  const renderLegend = (props) => {
    const { payload } = props;
    console.log(payload[0].color)

    return (
      <div className="legend-container">
        {payload.map((entry, index) => (
          <div
            className="legend-item"
            style={{ color: `${entry.color}` }}
            key={`item-${index}`}
          >
            {entry.payload.currencyId}: {entry.payload.quantity}
          </div>
        ))}
      </div>
    );
  };

  return (
    <div className="portfolioMakeup-container">
      <h2 id="portfolioMakeup">Current Account Balances</h2>
      <div className="pieChart">
        {userBalance && (
          <ResponsiveContainer minWidth="250px" minHeight="250px">
            <PieChart width={400} height={400}>
              <Pie
                data={userBalance}
                dataKey="quantity"
                isAnimationActive={false}
                cx="50%"
                cy="50%"
                outerRadius={80}
                fill="#8884d8"
                label={(entry) =>
                  `${entry.quantity.toLocaleString("en-US")} ${
                    entry.currencyId
                  }`
                }
              >
                {userBalance.map((entry, index) => (
                  <Cell
                    key={`cell-${index}`}
                    fill={COLORS[index % COLORS.length]}
                  />
                ))}
              </Pie>
              <Legend content={renderLegend} verticalAlign="bottom" height={36} />
              <Tooltip content={<CustomTooltip />} />
            </PieChart>
          </ResponsiveContainer>
        )}
      </div>
    </div>
  );
}

export default PortfolioGraph;
