using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;

public class StartGame : MonoBehaviour
{
    public PlayerManager playerManager;

    public void OnStart()
    {
        NetworkIdentity networkIdentity = NetworkClient.connection.identity;
        playerManager = networkIdentity.GetComponent<PlayerManager>();
        //if (playerManager.gameManager.isMyTurn == true)
        //{
        playerManager.CmdDestroyDie();
        //}
        
    }

}
