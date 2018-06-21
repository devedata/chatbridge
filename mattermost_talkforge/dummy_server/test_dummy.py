import requests


r = requests.post(
    "http://127.0.0.1:8088",
    json={
        "token":"73qxuufmofnux81ww5yfe36w1h",
        "team_id":"nqpx4xaibiyuxkx1tn64ef4wtc",
        "team_domain":"test-team",
        "channel_id":"o55g4t4re7nt8e6abddonu65zh",
        "channel_name":"cliq-test",
        "timestamp":1528370628342,
        "user_id":"ok68x1ycz3rr7pkupgfgtsfnsw",
        "user_name":"test_admin",
        "post_id":"6rwm5xyskpbi58rwkocm8hmc9y",
        "text":"a lot of images!",
        "trigger_word":"",
        "file_ids":"5kxofkrbwpf3mmpce9jetmrfsr,g9erqn7x4p8imphfycthxogu4o"
    },
)

print(r.status_code, r.reason)
