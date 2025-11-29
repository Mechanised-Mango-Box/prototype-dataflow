using Godot;
using System;
using System.Collections.Immutable;


public abstract class BaseNode
{
	public Vector2 Position;

	public PinConfig<VariableAny> GetInputPin(int index) => GetInputPins()[index];
	public abstract ImmutableArray<PinConfig<VariableAny>> GetInputPins();

	public PinConfig<VariableAny> GetOuputPin(int index) => GetOuputPins()[index];
	public abstract ImmutableArray<PinConfig<VariableAny>> GetOuputPins();

	public abstract void Evaluate(DataFlowMachine dfm);
}

public abstract class ActuatorNode : BaseNode
{
	public abstract void Actuate(DataFlowMachine dfm);
}

public sealed class VarReadNode : BaseNode
{
	public override void Evaluate(DataFlowMachine dfm)
	{
		VariableString variableLabel = dfm.GetInputPinValue("label");
		VariableAny variableValue = dfm.GetUserVariable(variableLabel.Value);
		dfm.SetOutputPinValue("value", variableValue);
	}
	public override ImmutableArray<PinConfig<VariableAny>> GetInputPins() => [new("name")];
	public override ImmutableArray<PinConfig<VariableAny>> GetOuputPins() => [new("value")];
}
public sealed class VarWriteNode : ActuatorNode
{
	public override void Actuate(DataFlowMachine dfm)
	{
		VariableString variableLabel = dfm.GetInputPinValue(this, "label");
		VariableAny variableValue = dfm.GetInputPinValue("value");
		dfm.SetUserVariable(variableLabel, variableValue);
	}

	public override void Evaluate(DataFlowMachine dfm) { }
	public override ImmutableArray<PinConfig<VariableAny>> GetInputPins() => [new("name"), new("value")];
	public override ImmutableArray<PinConfig<VariableAny>> GetOuputPins() => [];
}
public sealed class PrintNode : ActuatorNode
{
	public override void Actuate(DataFlowMachine dfm)
	{
		VariableAny variableValue = dfm.GetInputPinValue("value");
		GD.Print(variableValue);
	}

	public override void Evaluate(DataFlowMachine dfm) { }
	public override ImmutableArray<PinConfig<VariableAny>> GetInputPins() => [new("value")];
	public override ImmutableArray<PinConfig<VariableAny>> GetOuputPins() => [];
}

// {

// 	public ImmutableArray<PinConfig<UserVariable>> GetArgPins() => Tag switch
// 	{
// 		OpCode.PRINT => [new PinConfig<VariableAny>("input")],

// 		OpCode.PRODUCT => [
// 				new PinConfig( "in_a", UserVariable.BOOL),
// 				new PinConfig( "in_b", UserVariable.BOOL)
// 			   ],

// 		OpCode.SUM => [
// 			new PinConfig( "in_a", UserVariable.BOOL),
// 			new PinConfig( "in_b", UserVariable.BOOL)
// 		   ],
// 	};

// public ImmutableArray<PinConfig<UserVariable>> GetResultPins() => Tag switch
// {
// 	OpCode.PRINT => ImmutableArray<PinConfig>.Empty,

// 	OpCode.VAR_READ => [new PinConfig("data", UserVariable.BOOL)],
// 	OpCode.VAR_WRITE => ImmutableArray<PinConfig>.Empty,

// 	OpCode.PRODUCT => [new PinConfig("out", UserVariable.BOOL)],

// 	OpCode.SUM => [new PinConfig("out", UserVariable.BOOL)],
// };

// public bool HasOutput() => GetResult() is not null; 
// }
