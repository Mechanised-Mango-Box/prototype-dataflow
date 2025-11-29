using System;

public readonly record struct PinConfig<T>(string PinLabel) where T : VariableAny;
