export type LogLevel ="DEBUG" | "INFO" | "WARNING" | "ERROR"

export type AgentLogs = {
    id:string;
    level:LogLevel;
    message:string;
    timestamp:string;
}

export type AgentLogsPaginate = {
  limit: number;
  offset: number;
}

export type AgentLogsFilter = {
  fromDate: Date
  toDate: Date
  level: string
}

export type AgentLogsResponse = {
  logs: AgentLogs[]
  agentLogsFilter: AgentLogsFilter
  agentLogsPaginate:AgentLogsPaginate 
  count: number
}