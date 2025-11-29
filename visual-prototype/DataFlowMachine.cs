using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Linq;
using Godot;

public class DataFlowMachine
{
    public readonly BoardConfig Board;

    public readonly Dictionary<PinAddress, VariableAny> NodeOutputTable;
    public readonly Dictionary<string, VariableAny> UserVariableTable;

    public DataFlowMachine(BoardConfig board)
    {
        Board = board;

        // Embedded from board
        UserVariableTable = new(board.InitialUserVariables);
        NodeOutputTable = new();
    }

    public void Tick()
    {
        EvaluateGraph();

        foreach (var actuator in Board.Nodes.Values.OfType<ActuatorNode>()) actuator.Actuate(this);
    }
    private void EvaluateGraph()
    {
        /// Add all nodes with no dependencies to frontier
        List<BaseNode> frontier = [];
        frontier.AddRange(Board.Nodes.Values.Where(node => node.GetResultPins().Length == 0));

        /// BFS-like over nodes
        while (frontier.Count > 0)
        {
            bool foundAnyProcessableNode = false;

            foreach (var node in frontier)
            {
                if (IsDependenciesFulfilled(node))
                {
                    node.Evaluate(this);
                    frontier.Remove(node);
                    foundAnyProcessableNode = true;
                    break;
                }
            }

            if (!foundAnyProcessableNode)
            {
                throw new Exception("Invalid DAG (probs? deadlock/cycle)");
            }
        }
    }

    public bool IsDependenciesFulfilled(BaseNode node)
    {
        /// All args have been connected and have results
        ImmutableArray<PinConfig<VariableAny>> inputPins = node.GetArgPins();
        ImmutableArray<PinAddress> inputPinAddresses = (ImmutableArray<PinAddress>)inputPins.Select(inputPin => new PinAddress(node.Id, inputPin.PinLabel));

        if (inputPinAddresses.Length == 0)
        {
            return true;  /// Has no dependencies
		}

        /// Go back up the chain:
        /// [source node] -----> (edge) -----> [node]
        return inputPinAddresses.All(argPin =>
            Board.Edges.TryGetValue(argPin, out var sourceEdge) &&
            Board.Nodes.TryGetValue(sourceEdge.Source.OwnerId, out var sourceNode) &&
            sourceNode.HasOutput()
        );
    }

    public UserVariable GetInputPinValue(BaseNode node, string label)
    {
        VariableAny variable;

        variable = Board.EmbeddedVariables[new(node.Id, label)];
        if (variable != null)
        {
            return variable;
        }

        variable = Board.InitialUserVariables[new(node.Id, label)];
        if (variable != null)
        {
            return variable;
        }

        throw new Exception();
    }

    public VariableAny GetUserVariable(string value)
    {
        throw new NotImplementedException();
    }

    public void SetOutputPinValue(string v, VariableAny variableValue)
    {
        throw new NotImplementedException();
    }
    // private void Actuate(BaseNode node)
    // {
    //     switch (node.Tag)
    //     {
    //         case OpCode.PRINT:
    //             {
    //                 GD.Print("INPUT PIN VALUE"); // todo
    //                 break;
    //             }
    //         case OpCode.VAR_READ: break;
    //         case OpCode.VAR_WRITE:
    //             {
    //                 string variableName = "fsedf"; // = node.inputs["Varaible Name"]
    //                 VariableAny variableValue = new VariableNothing(); //= node.inputs["Value"]
    //                 UserVariableTable[variableName] = variableValue;
    //                 break;
    //             }
    //         case OpCode.PRODUCT: break;
    //         case OpCode.SUM: break;
    //     }
    // }

    // public void Evaluate(BaseNode node)
    // {
    //     switch (node.Tag)
    //     {
    //         case OpCode.PRINT: break;
    //         case OpCode.VAR_READ:
    //             {
    //                 string variableName = "fsedf"; // = node.inputs["Varaible Name"]
    //                 VariableAny variableValue = UserVariableTable[variableName];
    //                 PinAddress outputPin = new(node.Id, "result");
    //                 NodeOutputTable[outputPin] = variableValue;
    //                 break;
    //             }
    //         case OpCode.VAR_WRITE: break;
    //         case OpCode.PRODUCT:
    //             {
    //                 // get a
    //                 // get b
    //                 // do and
    //                 // set output
    //                 break;
    //             }
    //         case OpCode.SUM:
    //             {
    //                 // get a
    //                 // get b
    //                 // do or
    //                 // set output
    //                 break;
    //             }
    //     }
    // }
}