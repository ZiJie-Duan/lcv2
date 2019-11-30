package main
import (
        "strconv"
        "os"
        "context"
        "fmt"
        "log"
        "google.golang.org/grpc"
        "v2ray.com/core/app/proxyman/command"
        "v2ray.com/core/common/protocol"
        "v2ray.com/core/common/serial"
        "v2ray.com/core/proxy/vmess"
)


var EMAIL string
var UUID string
var API_ADDRESS string
var API_PORT int
var INBOUND_TAG string
var LEVEL uint32
var ALTERID uint32

/*
const (
        API_ADDRESS = "127.0.0.1"
        API_PORT    = 10085
        INBOUND_TAG = "proxy"
        LEVEL   = 0
        ALTERID = 32
)
*/

func addUser(c command.HandlerServiceClient) {
        resp, err := c.AlterInbound(context.Background(), &command.AlterInboundRequest{
                Tag: INBOUND_TAG,
                Operation: serial.ToTypedMessage(&command.AddUserOperation{
                        User: &protocol.User{
                                Level: LEVEL,
                                Email: EMAIL,
                                Account: serial.ToTypedMessage(&vmess.Account{
                                        Id:               UUID,
                                        AlterId:          ALTERID,
                                        SecuritySettings: &protocol.SecurityConfig{Type: protocol.SecurityType_AUTO},
                                }),
                        },
                }),
        })
        if err != nil {
                log.Printf("failed to call grpc command: %v", err)
        } else {
                log.Printf("ok: %v", resp)
        }
}
func removeUser(c command.HandlerServiceClient) {
        resp, err := c.AlterInbound(context.Background(), &command.AlterInboundRequest{
                Tag: INBOUND_TAG,
                Operation: serial.ToTypedMessage(&command.RemoveUserOperation{
                        Email: EMAIL,
                }),
        })
        if err != nil {
                log.Printf("failed to call grpc command: %v", err)
        } else {
                log.Printf("ok: %v", resp)
        }
}


func main() {
        /*此程序用于辅助python调用v2ray api的工具
        此程序传参顺序为
        mod EMAIL UUID API_ADDRESS API_PORT 
        INBOUND_TAG LEVEL ALTERID
        mod为程序添加用户/删除用户的标记符（add/del）
        */
        var cmds []string

        for _, args := range os.Args{
                cmds = append(cmds, args)
        }

        EMAIL = cmds[2]
        UUID  = cmds[3]
        API_ADDRESS = cmds[4]
        API_PORT,_    = strconv.Atoi(cmds[5])
        INBOUND_TAG = cmds[6]
        a,_ := strconv.Atoi(cmds[7])
        b,_ := strconv.Atoi(cmds[8])
        LEVEL  = uint32(a)
        ALTERID = uint32(b)

        if cmds[1] == "add"{
                fmt.Printf("add_mode")
                cmdConn, err := grpc.Dial(fmt.Sprintf("%s:%d", API_ADDRESS, API_PORT), grpc.WithInsecure())
                if err != nil {
                        panic(err)
                }

                hsClient := command.NewHandlerServiceClient(cmdConn)
                addUser(hsClient)
        }else{
                fmt.Printf("del_mode")
                cmdConn, err := grpc.Dial(fmt.Sprintf("%s:%d", API_ADDRESS, API_PORT), grpc.WithInsecure())
                if err != nil {
                        panic(err)
                }

                hsClient := command.NewHandlerServiceClient(cmdConn)
                removeUser(hsClient)
        }

}
